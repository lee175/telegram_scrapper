# telegram_scrapper

Scrape users from one group. Add to target group

limit: 30-50

get api for a number via : https://my.telegram.org/api

- add the api and hash to the config files

Telegram Restrictions

- max 50 users per account
- account should be a member in both target and source channels

#### config.json

Create a config.json file in root directory
use the config.example.json as reference. Fill the **group_target** with group id where you want to add users to. Fill the **group_source** with group id from where you want to fetch users from.

> To get the **group_id** of the target and source group, you can open telegram in the browser and inspect the group name in the left bar. Find the html element and look for data-peer-id="".

**Note**: fill the **group_target** and **group_source** in the config.json, this prevents unnecesssary member fetching from other groups joined by the given account(config.json)

#### Join_group

Logs into the given group/channels using invite link.
Use this before fetching the data. As user need to be a member of a group to fetch data.

This works for public group/channel

> Currently this works for a single accounts(config.json). Will update the code for looping through all accounts later.

#### leave_group

Logs out from the given group/channels using the invite link.
Use this after bot is done adding the group members to the target group.

This works for public group/channel

> Currently this works for a single accounts(config.json). Will update the code for looping through all accounts later.

#### init_session

this will log into the accounts provided in the accounts(config.json)
