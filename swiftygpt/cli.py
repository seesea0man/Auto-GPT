"""Example agents for the SwiftyGPT library."""
import click


@click.group()
def main() -> None:
    """SwiftyGPT commands."""
    pass


@main.command()
def start() -> None:
    """Run the test agent."""
    import asyncio

    import swiftygpt.agent_factory
    from swiftygpt.messaging.queue_channel import QueueChannel

    channel = QueueChannel("channel1", "localhost", 8080)
    agent1 = swiftygpt.agent_factory.build_agent("agent1", channel)
    agent2 = swiftygpt.agent_factory.build_agent("agent2", channel)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(agent1.run(), agent2.run()))


@main.command()
@click.option("--host", default="0.0.0.0", help="Host address.")
@click.option("--port", default=8000, help="Listening port.")
def run_server(host: str, port: int):
    """Run the SwiftyGPT server."""
    import uvicorn

    import swiftygpt.server

    uvicorn.run(swiftygpt.server.app, host=host, port=port)


########################################
########## EXAMPLE AGENTS ##############
########################################


@click.group()
def examples() -> None:
    """Pre-defined agents to showcase the Auto-GPT library."""
    pass


@examples.command()
def entrepreneur() -> None:
    """
    This agent is an entrepreneur.

    The objective of this agent is to create and manage a profitable business. It showcases
    the library's capabilities in strategic decision making, resource management, and
    financial calculations.
    """
    print("Hello, I'm an entrepreneur!")


@examples.command()
def software_engineer() -> None:
    """
    This agent is a software engineer.

    The objective of this agent is to design, develop, and maintain software systems. It
    showcases the library's capabilities in algorithmic thinking, code generation, and
    debugging.
    """
    print("Hello, I'm a software engineer!")


@examples.command()
def code_reviewer() -> None:
    """
    This agent is a code reviewer.

    The objective of this agent is to review and improve the quality of software code. It
    showcases the library's capabilities in code analysis, identifying best practices, and
    spotting potential bugs.
    """
    print("Hello, I'm a code reviewer!")


@examples.command()
def marketing() -> None:
    """
    This agent is a marketer.

    The objective of this agent is to promote products or services and attract customers. It
    showcases the library's capabilities in market research, advertising strategy, and
    customer engagement.
    """
    print("Hello, I'm a marketer!")


@examples.command()
def product_manager() -> None:
    """
     This agent is a Product Manager.


    This agent's objective is to simulate the role of a product manager.
    It showcases the library's ability to implement high-level decision making and strategic planning functionality.
    """
    print("Hello, I'm a product manager!")


@examples.command()
def investor() -> None:
    """
    This agent is an Investor.

    This agent's objective is to simulate the role of an investor.
    It demonstrates the library's capacity for financial analysis and risk assessment.
    """
    print("Hello, I'm an investor!")


@examples.command()
def hr() -> None:
    """
    This agent is an human resources manager.

    This agent's objective is to simulate the role of a human resources manager.
    It highlights the library's capabilities in managing and organizing human resources data and tasks.
    """
    print("Hello, I'm a human resources manager!")


main.add_command(examples)


if __name__ == "__main__":
    main()
