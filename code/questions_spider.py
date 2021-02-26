"""
爬取 Leetcode 中题目的：[标题，难度，类型]
"""
import click
import asyncio
import pandas as pd
from pyppeteer import launch
from tqdm import tqdm

rows = []


async def search_q(search, debug):
    """找到该题目的url，返回page和 url."""
    if debug:
        headless = False
    else:
        headless = True
    click.echo('正在打开浏览器.')
    browser = await launch(headless=headless)
    page = await browser.newPage()
    url = 'https://leetcode-cn.com/problems/two-sum/'
    # url = 'https://leetcode-cn.com/problems/intersection-of-two-linked-lists/'
    await page.goto(url)
    for _ in tqdm(range(200)):
        if debug:
            await asyncio.sleep(1)
        row = {}
        # 题目
        e_title = (await page.xpath("//h4[@class='css-10c1h40-Title eugt34i1']/a//text()"))
        row["title"] = await get_texts(e_title)

        # 难度
        e_level = (await page.xpath("//span[@class='css-1p5igso-Difficulty e1o5n5iy1'][2]"))
        row["level"] = await get_texts(e_level)

        # 题目类型
        e_types = await page.xpath("//div[@class='topic-tags__1S89']//text()")
        row["type"] = await get_texts(e_types)

        # 加入记录
        rows.append(row)

        # 下一页
        next_button = (await page.xpath("//button[@id='next-question-btn']"))[0]
        await next_button.click()

    # detail_url = await (await e_title.getProperty('href')).jsonValue()
    return browser, page


async def get_texts(eles):
    rst = []
    for e in eles:
        rst.append(await get_text(e))
    return rst


async def get_text(ele):
    """从ElementHandle提取出文字."""
    return await (await ele.getProperty('textContent')).jsonValue()


def main():
    """程序入口."""
    asyncio.get_event_loop().run_until_complete(search_q("1", True))

    df = pd.DataFrame(rows)
    df.to_csv("questions.csv", index=False)


if __name__ == '__main__':
    main()
