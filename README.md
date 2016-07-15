# GroupMe Bots
A like-bot and analysis-bot for GroupMe group chats. These bots are built on Python and use the GroupMe API.

[![Maintenance Intended](http://maintained.tech/badge.svg)](http://maintained.tech/)

## Use
You will need:
* Your account access token
	* You can get it by signing into here: 	`https://dev.groupme.com/bots`
	* Click the `access token` button on the right side of the top navigation bar
	* Copy and paste the access token into the console when requested by the program
* A chat group to like-bot/analyze
	* The group must be one of the user's ten groups with the most recent activities 
 
## LikeBot
An original like bot for group chats. It can like all the messages of a specific user or dislike all the messages. In the likebot.py script, there are options in the code to configure it for more specific filters in terms of which messages to likebot, such as opening the likebot to affecting all users (will be connected with UI in later features).

## Analysis Bot
An analysis bot for group chats. Includes code from `https://github.com/cdzombak/groupme-tools/blob/master/README.md`. Allows for the robust analysis of GroupMe chat groups.

The analysis bot can return the following measures for each user and the group as a whole:
* Nickname, 
* Total messages sent in group,
* Like count, 
* Likes per message,
* Average likes received per message, 
* Total words sent, 
* Dictionary of likes received from each member
* Dictionary of shared likes, 
* Total likes given

## GroupMe API
These scripts use GroupMe's public API. GroupMe's API documentation can be found here: `https://dev.groupme.com/docs/v3`.


# License
The MIT License (MIT)

Copyright (c) 2016 Eric Zhao

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

**Major contributions**

Includes modified contributions from `https://github.com/cdzombak/groupme-tools/blob/master/README.md`