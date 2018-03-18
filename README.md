# onegram
[![Build Status](https://travis-ci.org/pauloromeira/onegram.svg?branch=master)](https://travis-ci.org/pauloromeira/onegram)

A simplistic api-like instagram **bot** powered by [requests](https://github.com/requests/requests).

### *Warnings!*
* **Under development**, not stable yet!
* Rate limits are not configured properly, so be respectful to not get banned!

## Installing and running
1. Clone this repo: `git clone https://github.com/pauloromeira/onegram.git`
2. Make sure you have python 3.6 installed on your machine
3. Install pipenv and dependencies:
    ```sh
    pip install pipenv
    cd onegram
    pipenv install
    ```
4. Place your script inside the project root directory and run it:
    ```sh
    pipenv run python script.py
    ```

## Examples
#### Follow me :wink:
```py
from onegram import follow

follow('<me>')
```

#### Like all my posts :joy:

```py
from onegram import like, posts

for post in posts('<me>'):
  like(post)
```

#### Who likes you most? :open_mouth:
```py
from collections import defaultdict
from operator import itemgetter

from onegram import posts, likes

rank = defaultdict(int)
for post in posts():
    for like_info in likes(post):
        username = like_info['username']
        rank[username] += 1

rank = sorted(rank.items(), key=itemgetter(1), reverse=True)

print(rank[:10]) # TOP 10!
```

#### Explicit login (optional)
```py
from onegram import Login, posts

with Login(username='user', password='pass'):
  user_posts = list(posts())
  other_posts = list(posts('other'))
```

##### Also possible
```py
from onegram import *

login()

last_post = next(posts())
post_likes = list(likes(last_post))

logout()
```

## Cheatsheet
The set of functions are divided into queries and actions. For some queries
the user is optional, with default set to the logged user.

|Query|Argument(s)||Action|Argument(s)|
|-|-|-|-|-|
|`user_info`|`[user]`||`follow`|`user`|
|`followers`|`[user]`||`unfollow`|`user`|
|`following`|`[user]`||`like`|`post`|
|`posts`|`[user]`||`unlike`|`post`|
|`post_info`|`post`||`comment`|`comment[, post]`|
|`likes`|`post`||`uncomment`|`comment[, post]`|
|`comments`|`post`||`save`|`post`|
|`feed`|||`unsave`|`post`|
|`explore`|||||

## Tips
  * Create a `.env` file with your credentials at project root directory,
  so you don't have to type it:
    ```sh
    INSTA_USERNAME=username
    INSTA_PASSWORD=password
    ```
