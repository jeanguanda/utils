import argparse
import sys
import json
import requests
from urllib.parse import urlparse

# PUT your API TOKEN on this variable
api_token = ""

# API URL base
api_url_base = "https://api.pingdom.com/api/3.1/"

# Default Headers
headers = {"Authorization": "Bearer {0}".format(api_token)}

# Function to list the current checks from Pingdom
def get_checks():
    api_url = "{0}checks".format(api_url_base)
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        checks = json.loads(response.content.decode("utf-8"))
        if checks["counts"]["total"] < 1:
            print("There's no UPTIME checks configured!!!")
        else:
            print("Here are the current checks: ")
            for items in checks["checks"]:
                print(
                    "ID: {} - Name: {} - Status: {}".format(
                        items["id"], items["name"], items["status"]
                    )
                )
            print(
                "------------------------------------------------------------------------------------"
            )
            print("Total: {}".format(checks["counts"]["total"]))
    else:
        return (
            (
                "[?] Unexpected error: [HTTP {0}]: Content: {1}".format(
                    response.status_code, response.content
                )
            ),
        )


# Function to create new checks


def put_checks(file):
    cnt = 0
    api_url = "{0}checks".format(api_url_base)
    # Open the file and parse the information to work correctly
    # See the Readme file to see the file format
    try:
        with open(file, "r") as fileAdd:
            for linefile in fileAdd:
                cnt += 1
                lineSep = linefile.split(",")
                URLFull = lineSep[1]
                urlParsed = urlparse(URLFull)
                if not urlParsed.path:
                    urlPath = "/"
                else:
                    urlPath = urlParsed.path

                # Variable to create the JSON information to add the check.
                # You can add or remove config options (get more information at https://docs.pingdom.com/api/#tag/Checks/paths/~1checks/post)
                new_check = {
                    "name": lineSep[0],
                    "host": urlParsed.netloc,
                    "url": urlPath,
                    "sendnotificationwhendown": 6,
                    "notifyagainevery": 0,
                    "notifywhenbackup": True,
                    "resolution": 1,
                    "probe_filters": "region: LATAM",
                }
                # If the URL has https, then the check is created with HTTPS options
                if urlParsed.scheme == "https":
                    new_check.update(
                        {
                            "type": "http",
                            "verify_certificate": True,
                            "encryption": True,
                            "port": "443",
                            "ssl_down_days_before": 15,
                        }
                    )
                # IF the URL starts with http, then the check is create with HTTP options
                elif urlParsed.scheme == "http":
                    new_check.update({"type": "http", "port": "80"})

                # Execute the POST to create the new checks
                response = requests.post(api_url, headers=headers, json=new_check)
                if response.status_code == 200:
                    resultAddCheck = json.loads(response.content.decode("utf-8"))
                    for k, v in resultAddCheck.items():
                        print(
                            "Added: {} - {} - {}".format(v["id"], v["name"], URLFull)
                        ),
                else:
                    return (
                        (
                            "[?] Unexpected Error: [HTTP {0}]: Content: {1}".format(
                                response.status_code, response.content
                            )
                        ),
                    )
    except FileNotFoundError:
        print("File {} does not exist".format(file))
    print(
        "\n---------------------------------------------------------------------------------------------------------------"
    )
    print("Total new checks added: {}".format(cnt))


# Main function using args to use the script
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create UPTIME checks at Pingdom")
    parser.add_argument(
        "-l", "--list", action="store_true", help="List UPTIME checks from Pingdom"
    )
    parser.add_argument(
        "-a",
        "--add",
        action="store_true",
        help="Add new entries, requires additional args for file path",
    )
    parser.add_argument(
        "-f",
        "--file",
        metavar="filePath",
        type=str,
        help="Path for the URL lists file, requires -a/--add arg",
    )
    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        parser.exit()
        args = parser.parse_args()

    if args.add and (args.file is None):
        parser.error("-a/--add requires -f/--file argument with the file path")

    if args.list:
        get_checks()

    if args.add and args.file:
        add_check = put_checks(args.file)
