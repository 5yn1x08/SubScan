#!/usr/bin/env python

import asyncio
import aiohttp
import re
import argparse
from colorama import Fore, Style, init
from pyfiglet import Figlet

init(autoreset=True)  # Autoreset colorama styles after each print


def print_figlet_text(text, font="slant"):
    print(Figlet(font=font).renderText(text))


def strip_ansi_codes(text):
    # Target only color codes used by colorama for foreground and background colors
    ansi_escape = re.compile(r"\x1b\[[0-9;]*m")
    return ansi_escape.sub("", text)


async def scan_target(session, target, output_file):
    url = f"https://{target}"
    try:
        async with session.get(url, timeout=10) as response:
            status_code = response.status
            status_color = Fore.GREEN if 200 <= status_code < 300 else Fore.RED

            result = f"Target: {target} | Status Code: {status_color}{status_code}{Style.RESET_ALL}\n"
            print(result, end="")

            # Save the result to the output file without color codes
            with open(output_file, "a") as file:
                file.write(strip_ansi_codes(result))

            # Add more processing based on the response if needed
    except aiohttp.ClientError as e:
        error_message = (
            f"Error connecting to {target}: {e} | Status Color: {Fore.RED}\n"
        )
        print(error_message, end="")

        # Save the error message to the output file without color codes
        with open(output_file, "a") as file:
            file.write(strip_ansi_codes(error_message))
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


async def main():
    parser = argparse.ArgumentParser(
        description="Scan targets for alive subdomains."
    )
    parser.add_argument(
        "domain_file", metavar="DOMAIN_FILE", type=str, help="Domain file name"
    )
    parser.add_argument(
        "-o",
        "--output",
        metavar="OUTPUT_FILE",
        type=str,
        help="Output file name",
        required=True,
    )
    args = parser.parse_args()

    subdomains = []
    with open(args.domain_file, "r") as file:
        subdomains = file.read().splitlines()

    async with aiohttp.ClientSession() as session:
        tasks = [scan_target(session, target, args.output) for target in subdomains]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    text_to_print = "SubScan"
    font_to_use = "slant"

    print_figlet_text(text_to_print, font_to_use)

    asyncio.run(main())
