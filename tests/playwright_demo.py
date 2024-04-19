from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://github.com/meilisearch/meilisearch/blob/main/README.md')
    # page.wait_for_event('domcontentloaded')
    selectors = [
        "#repository-container-header",
        ".js-header-wrapper",
        ".dAneXo",
        ".eIgvIk",
        ".ePiodO",
        ".gvCnwW",
        ".Box-sc-g0xbh4-0.eYedVD"
    ]
    # remove elemtents
    for selector in selectors:
        for elem in page.query_selector_all(selector):
            elem.evaluate('e => e.remove()')

    input("")
    # save as PDF
    page.pdf(path='meilisearch.pdf')