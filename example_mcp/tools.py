from fastmcp import FastMCP

mcp = FastMCP("sales-tools")


@mcp.tool()
def get_sales(start_date: str, end_date: str) -> str:
    return f"{start_date}~{end_date} 매출 데이터 조회 결과"


@mcp.tool()
def detect_anomaly(data: str) -> str:
    return "3월 22일 매출이 평소 대비 42% 급증"


@mcp.tool()
def post_slack(channel: str, text: str) -> str:
    return f"{channel} 채널에 전송 완료: {text}"


if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
