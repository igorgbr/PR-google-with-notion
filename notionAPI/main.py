import requests
import json

from requests.api import request


def readDatabase(databaseId, headers):
    # readUrl = f"https://api.notion.com/v1/databases/{databaseId}/query"
    readUrl = f"https://api.notion.com/v1/databases/{databaseId}/query"

    res = requests.request("POST", readUrl, headers=headers)
    data = res.json()
    print(res.status_code)

    with open("./db.json", "w", encoding="utf8") as file:
        json.dump(data, file, ensure_ascii=False)

    with open("./db.json") as json_file:
        data = json.load(json_file)
        print(data["results"][1])


def createPage(databaseId, headers):
    createUrl = "https://api.notion.com/v1/pages"

    newPageData = {
        "parent": {"database_id": databaseId},
        "properties": {
            "Name": {"title": [{"text": {"content": "review"}}]},
            "Value": {"rich_text": [{"text": {"content": "Amazing"}}]},
            "Status": {"rich_text": [{"text": {"content": "Active"}}]},
        },
    }

    data = json.dumps(newPageData)

    res = requests.request("POST", createUrl, headers=headers, data=data)
    print(res.status_code)
    # print(res.text)


def updatePage(pageId, headers):
    pageUpdate = f"https://api.notion.com/v1/pages/{pageId}"

    updateData = {
        "properties": {"Value": {"rich_text": [{"text": {"content": "Sara"}}]}}
    }

    data = json.dumps(updateData)
    res = requests.request("PATCH", pageUpdate, headers=headers, data=data)

    print(res.status_code)
    # print(res.text)


def requestPage(pageId, headers):
    page_request = f"https://api.notion.com/v1/blocks/{pageId}/children"
    res = requests.request("GET", page_request, headers=headers)

    data = res.json()
    print(res.status_code)

    with open("./db.json", "w", encoding="utf8") as file:
        json.dump(data, file, ensure_ascii=False)

    with open("./db.json") as json_file:
        data = json.load(json_file)

        # print(len(data["results"]))
        print(data["results"])


def requestPages(page_blocks, headers):
    blocklists = []
    for block in page_blocks:
        page_request = f"https://api.notion.com/v1/blocks/{block}/children"
        res = requests.request("GET", page_request, headers=headers)

        data = res.json()

        with open("./db.json", "w", encoding="utf8") as file:
            json.dump(data, file, ensure_ascii=False)

        with open("./db.json") as json_file:
            data = json.load(json_file)

            if len(data["results"]) > 1:
                blocklists.append(len(data["results"]) - 1)
            else:
                blocklists.append(len(data["results"]))

    print("Notion Success", res.status_code)
    return blocklists
