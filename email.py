import smtplib
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("email")





s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("email-id", "email password")




@mcp.tool()
def send_email(message: str):
    """this method sends an email with the message passed to it"""
    s.sendmail("f20190450p@alumni.bits-pilani.ac.in", "deepshbansal491@gmail.com", message)
    s.quit()
    return "Email sent successfully!"

if __name__ == "__main__":
    print("Starting the MCP Server")
    mcp.run(transport="stdio")
