from app.community.plugins.coin_price_chart_similarity_search.tools import TOOLS
from app.core.plugins import BasePlugin
from app.core.plugins.registry import ensure_plugin_registry
from app.core.plugins.tools import BaseTool

plugin_registry = ensure_plugin_registry()

@plugin_registry.register(name="coin-price-chart-similarity-search")
class CoinPriceChartSimilaritySearchPlugin(BasePlugin):
    name = "Coin Price Chart Similarity Search"
    description = "AI plugin for search coins similar to a given coin by price chart similarity."
    owner = "2snYEzbMckwnv85MW3s2sCaEQ1wtKZv2cj9WhbmDuuRD"
    price = 1000
    tools: type[list[BaseTool]] = TOOLS
    image_url = "https://fidrox-ai-assets.s3.eu-central-1.amazonaws.com/agent-avatars/chart-similarity-avatar.png"
    json_format = True
