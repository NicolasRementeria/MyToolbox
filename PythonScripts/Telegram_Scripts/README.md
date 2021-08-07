# PythonScripts

- get_telegram_groupmembers.py:
  - Description: Get all group members of a Telegram channel, and export it into a CSV

- interactive_telegram_client.py:
  - Branch of https://github.com/LonamiWebs/Telethon/blob/master/telethon_examples/interactive_telegram_client.py
  - What's different?: This updated script will save the latest messages of the selected chat/group to an Output.txt, at the script's folder
  - Description: Menu-based script, that in real time lets you interact with your account.
    - !h: prints the latest messages (message History). (updated)
    - !up  <path>: Uploads and sends the Photo from path.
    - !uf  <path>: Uploads and sends the File from path.
    - !d   <msg-id>: Deletes a message by its id
    - !dm  <msg-id>: Downloads the given message Media (if any).
    - !dp: Downloads the current dialog Profile picture.
    - !i:  Prints information about this chat.
