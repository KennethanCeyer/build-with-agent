import os
from typing import Any

from google.adk.cli.utils.envs import load_dotenv
from google.adk.tools import google_search

load_dotenv()

__all__ = [
    "google_search",
    "generate_theme_image",
]


async def generate_theme_image(
    prompt: str,
    tool_context=None,
) -> dict[str, Any]:
    from google import genai
    from google.genai import types as genai_types

    api_key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-3.1-flash-image-preview",
        contents=[prompt],
        config=genai_types.GenerateContentConfig(
            response_modalities=[genai_types.Modality.IMAGE],
        ),
    )

    image_bytes = None
    for part in response.candidates[0].content.parts:
        if part.inline_data:
            image_bytes = part.inline_data.data
            break

    if not image_bytes:
        return {"ok": False, "error": "이미지 생성 실패"}

    invocation_id = getattr(
        tool_context,
        "invocation_id",
        "default",
    )
    filename = f"theme-{invocation_id}.png"

    if hasattr(tool_context, "save_artifact"):
        await tool_context.save_artifact(
            filename,
            genai_types.Part.from_bytes(
                data=image_bytes,
                mime_type="image/png",
            ),
        )

    return {
        "ok": True,
        "filename": filename,
        "description": f"이미지가 {filename}으로 저장되었습니다.",
    }
