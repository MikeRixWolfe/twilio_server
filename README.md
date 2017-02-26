## Goals
This is a simple TwiML server to act as a JSON REST relay for Twilio. It supports single MMS attachments and can also be used as an endpoint for multiple Twilio accounts/numbers at once. It implments an extensible Flask-Restful architecture that allows easy modification to suit your needs; for example, publishing to Redis rather than writing to a SQLite database to implement a pub/sub architecture for use with other applications.

## Installation
Install python 2.7.x and SQLite, then run the following

     git clone https://github.com/MikeRixWolfe/twilio_server.git
     sudo pip2 install -r requirements.txt

## Setup
Rename `app.cfg.default` to `app.cfg` and enter desired information, and run `python db_setup.py`.

## Usage
#### Server
Run `python run.py` in a screen/tmux session or with nohup/wsgi/whatever.
#### Client
Enter `http://yoursite.tld/twilioendpoint` as the TwiML endpoint for your Twilio number's messages to have the messages sent to the server.

Browse/cUrl/whatever `http://yoursite.tld/messages/<account_sid>/<phone_number>` to retreive messages for that Twilio account and number.

## Requirements
* Python 2.7.x
* SQLite
* Flask
* Flask-Restful
* Flask-SQLAlchemy

## License
This software is licensed under the **GPL v3** license. The terms are as follows:
     
     twilio_server
     Copyright (C) 2017  Mike Rix Wolfe
     
     This program is free software: you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     
     This program is distributed in the hope that it will be useful,
     but WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
     GNU General Public License for more details.
     
     You should have received a copy of the GNU General Public License
     along with this program.  If not, see <http://www.gnu.org/licenses/>.
