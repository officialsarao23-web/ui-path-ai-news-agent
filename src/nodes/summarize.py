from uipath.platform import UiPath
from langchain_groq import ChatGroq


def _get_asset(name: str) -> str:
    sdk = UiPath()
    asset = sdk.assets.retrieve(name)
    return asset.value


def summarize_node(state):
    api_key = _get_asset("GROQ_API_KEY")
    llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=api_key)
    summaries = []
    for article in state.articles:
        prompt = (
            "Summarize the following in exactly 2 plain-English sentences:\n\n"
            f"{article['content']}"
        )
        response = llm.invoke(prompt)
        summaries.append({
            "title": article["title"],
            "summary": response.content,
            "url": article["url"],
        })
    return {"summaries": summaries}
