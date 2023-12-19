# Gemini CLI

The Gemini CLI is a command-line tool for interacting with Large Language Models (LLMs) in your terminal. It allows you to send and receive messages to and from LLMs, and to use them to generate text, translate 
languages, write different kinds of creative content, debug code, and more.

## Features

* Send and receive messages to and from LLMs
* Generate text
* Translate languages
* Write different kinds of creative content
* Debug code
* ... and more!

## Installation

To install the Gemini CLI, run the following command:

```
pip install gemini-cli
```

## Usage

To use the Gemini CLI, simply run the following command:

```
gemini
```

This will start the Gemini CLI and display a prompt. You can then use the following commands to interact with LLMs:

* **`send <model> <message>`:** Send a message to an LLM.
* **`generate <model> <prompt>`:** Generate text using an LLM.
* **`translate <model> <text> <target_language>`:** Translate text using an LLM.
* **`write <model> <prompt>`:** Write creative content using an LLM.
* **`debug <model> <code>`:** Debug code using an LLM.

## Examples

To send a message to an LLM, use the following command:

```
gemini send gemini Hello, world!
```

To generate text using an LLM, use the following command:

```
gemini generate gemini Write a poem about a cat.
```

To translate text using an LLM, use the following command:

```
gemini translate gemini Hello, world! Spanish
```

To write creative content using an LLM, use the following command:

```
gemini write gemini Write a short story about a detective investigating a murder mystery.
```

To debug code using an LLM, use the following command:

```
gemini debug gemini Find the bug in this code:

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
```

## Contributing

Contributions to the Gemini CLI are welcome! Please read the [contributing guidelines](https://github.com/example/gemini-cli/blob/main/CONTRIBUTING.md) before submitting a pull request.

## License

The Gemini CLI is licensed under the MIT License.
```

You can customize this README file to fit your specific needs. Be sure to include information about your package's features, installation instructions, usage instructions, and contributing guidelines.

I hope this helps!

Please note that the above examples use the `gemini` model as the default LLM. You can specify a different LLM by using the `-m` or `--model` option. For example:

```
gemini -m text-bison-001 send Hello, world!
```

This will send the message "Hello, world!" to the Text-Bison-001 model.

You can also use the `gemini` command to list the available LLMs:

```
gemini --list-models
```

This will print a list of all the LLMs that are currently supported by the Gemini CLI.


