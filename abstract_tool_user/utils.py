# region GPT Utils - query prompt
from enum import Enum


class PromptEngine(Enum):
    OpenAI = 1
    LangChain = 2
    GPTKit = 3


engine = PromptEngine.OpenAI


# todo: move to calmlib
def query_prompt(
    prompt: str,
    engine: PromptEngine = engine,
    warmup_messages: list[str] = None,
    system: str = "You're a helpful assistant",  # system message / prompt
    model="gpt-3.5-turbo",
    **kwargs,
) -> str:
    if engine == PromptEngine.OpenAI:
        # make a call to the openai api
        return _query_prompt_openai(
            prompt,
            model=model,
            system=system,
            warmup_messages=warmup_messages,
            **kwargs,
        )
    elif engine == PromptEngine.LangChain:
        # make a call to the langchain api
        pass
    elif engine == PromptEngine.GPTKit:
        raise NotImplementedError("GPT Kit is not implemented yet.")
    else:
        raise ValueError(f"Unknown engine: {engine}")


# region 1 - openai api
def _query_prompt_openai(
    prompt: str,
    model="gpt-3.5-turbo",
    system="You're a helpful assistant",
    warmup_messages: list[str] = None,
    **kwargs,
) -> str:
    from dotenv import load_dotenv

    load_dotenv()  # init the environment variables - load the api key
    from openai import OpenAI

    messages = []
    messages.append(
        {
            "role": "system",
            "content": system,
        },
        # "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."
    )
    # check if the warmup messages are provided and are properly formatted
    for i, msg in enumerate(warmup_messages):
        if isinstance(msg, str):
            role = "user" if i % 2 == 0 else "assistant"
            msg = {"role": role, "content": msg}
        messages.append(msg)
    messages.append(
        {
            "role": "user",
            "content": prompt,
        },  # "Compose a poem that explains the concept of recursion in programming."
    )

    client = OpenAI()
    # todo: check that system is not a FewshotPrompt class instance
    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        **kwargs,
    )

    return completion.choices[0].message.content


# endregion 1 - openai api
# region 2 - langchain
def _query_prompt_langchain(
    prompt: str, model="gpt-3.5-turbo", system="You're a helpful assistant", **kwargs
) -> str:
    pass
    # I have done this somewhere already...
    # with a Fewshot prompt example..
    # I can reuse that code here
    # for now - let's just use the raw openai api


# endregion 2 - langchain
# region 3 - GPT Kit, GPT Engine (smart manager of tokens, quotas, RPM etc.)
def _query_prompt_gpt_kit(
    prompt: str, model="gpt-3.5-turbo", system="You're a helpful assistant", **kwargs
) -> str:
    raise NotImplementedError("GPT Kit is not implemented yet.")


# endregion 3 - GPT Kit, GPT Engine (smart manager of tokens, quotas, RPM
# endregion GPT Utils - query prompt
