from app.community.plugins.fidrox.utilities import FidroxRagUtility
from app.core.plugins.schemas import BaseToolInput
from app.core.plugins.tools import BaseTool


class FidroxRagInput(BaseToolInput):
    question: str


FidroxRagTool = BaseTool(
    name="fidrox-rag",
    description="Use this tool to answer questions about FidroxAI",
    args_schema=FidroxRagInput,
    utility=FidroxRagUtility(),
    examples=[
        {
            "request": "Who are you?",
            "response": "",
        },
        {
            "request": "What plugins do you have?",
            "response": "",
        }
    ]
)


TOOLS = [FidroxRagTool]
