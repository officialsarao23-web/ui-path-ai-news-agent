from uipath.platform import UiPath
from tavily import TavilyClient


def _get_asset(name: str) -> str:
    sdk = UiPath()
    asset = sdk.assets.retrieve(name)
    return asset.value


def fetch_news_node(state):
    api_key = _get_asset("TAVILY_API_KEY")
    client = TavilyClient(api_key=api_key)
    result = client.search(
        query="artificial intelligence AI news today",
        search_depth="advanced",
        max_results=5,
    )
    articles = [
        {"title": r["title"], "url": r["url"], "content": r["content"]}
        for r in result["results"]
    ]
    return {"articles": articles}
