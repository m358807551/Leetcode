# coding=utf-8

"""pyppeteer 版."""
import asyncio
import logging
from collections import OrderedDict

import click
import pandas as pd
from pyppeteer import launch


logger = logging.getLogger('leetcode')


@click.group()
def cli():
    pass


async def _a(search, debug=False):
    """
    爬虫入口.
    """
    browser, page, detail_url = await search_q(search, debug)
    solution_url = str(detail_url) + '/solution/'
    await page.goto(solution_url)
    click.echo(f'转到题目解答页: {solution_url}')

    solutions = []
    e_solution_titles = await page.xpath('//h3/a/span/span')
    for e_solution_title in e_solution_titles:
        solution_title = await get_text(e_solution_title)
        await e_solution_title.click()
        await asyncio.sleep(1)

        codes = []
        # await page.waitForXPath('//*[@id="lc-home"]/div/div[2]/div[1]/div/div[3]/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/h1')
        e_codes = await page.xpath("//pre/code")
        for e_code in e_codes:
            code = await get_text(e_code)
            # 没有 class 就不是完整题解
            if 'class' not in code:
                continue
            codes.append(code)
        codes.sort(key=lambda x: len(x))

        solution = OrderedDict()
        solution['title'] = solution_title
        solution['code'] = codes[0] if codes else ''
        solution['code_size'] = solution['code'].count('\n')
        solutions.append(solution)
        click.echo('已累计分析完{size}个解答'.format(size=len(solutions)))

    await browser.close()

    solutions.sort(key=lambda x: x['code_size'] or 999)
    shorted_solution = solutions[0]
    click.echo(
        '行数最短的题解有{min_code_size}行，在: {title}'.format(
            min_code_size=shorted_solution['code_size'],
            title=shorted_solution['title'],
        )
    )
    click.echo('\n' + shorted_solution['code'])

    df = pd.DataFrame(solutions)
    df.to_csv('solution.csv', index=False)


async def search_q(search, debug):
    """找到该题目的url，返回page和 url."""
    if debug:
        headless = False
    else:
        headless = True
    click.echo('正在打开浏览器.')
    browser = await launch(headless=headless)
    page = await browser.newPage()
    url = f'https://leetcode-cn.com/problemset/all/?search={search}'
    await page.goto(url)
    click.echo('正在搜索题目.')

    if debug:
        await asyncio.sleep(1)
    e_title = (await page.xpath('//*[@id="question-app"]/div/div[2]/div[2]/div[2]/table/tbody[1]/tr[2]/td[3]/span/div/a'))[0]
    detail_url = await (await e_title.getProperty('href')).jsonValue()
    return browser, page, detail_url


async def get_text(ele):
    """从ElementHandle提取出文字."""
    return await (await ele.getProperty('textContent')).jsonValue()


async def get_texts(eles):
    """从ElementHandle提取出文字."""
    texts = []
    for ele in eles:
        text = await get_text(ele)
        texts.append(text)
    return texts


@cli.command()
@click.option('--debug', '-d', default=False, help='是否启动debug模式：包括前台启动和加入额外的等待时间.', type=bool)
@click.argument('search')
def a(search, debug):
    """入口."""
    asyncio.get_event_loop().run_until_complete(_a(search, debug))


@cli.command()
@click.option('--debug', '-d', default=False, help='是否启动debug模式：包括前台启动和加入额外的等待时间.', type=bool)
@click.argument('search')
def q(search, debug):
    """生成题目."""
    asyncio.get_event_loop().run_until_complete(_q(search, debug))


async def _q(search, debug):
    browser, page, detail_url = await search_q(search, debug)
    click.echo(f'正在跳转详情页')
    await page.goto(str(detail_url))
    await page.waitForXPath("//div[@class='notranslate']")
    e = (await page.xpath("//div[@class='notranslate']"))[0]
    content = await get_text(e)
    await browser.close()

    click.echo(content)
    click.echo(detail_url)


if __name__ == '__main__':
    cli()
    # asyncio.get_event_loop().run_until_complete(start(72, debug=False))
