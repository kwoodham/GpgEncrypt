from fman import DirectoryPaneCommand, show_alert, show_prompt, load_json, save_json
from fman.url import as_human_readable
from gnupg import GPG
import os

# Kurt Woodham 25 July 2019
# This is as bare-bones a plugin as one gets: no eror checking,
# assumes default for gnupghome (home/.)

CONFIG_FILE_NAME = "default_recipient.json"


class GpgEncrypt(DirectoryPaneCommand):
	def __call__(self):
		fileName = as_human_readable( self.get_chosen_files()[0] )
		gpg = GPG()
		default_recipient = self._get_default_recipient()
		recipient, ok = show_prompt('Recipient', default = default_recipient)
		with open(fileName, 'rb') as f:
			status = gpg.encrypt_file(
				f, recipients = [ recipient ],
				output = fileName + '.gpg')
		show_alert('Status: ' + status.status)

	def _get_default_recipient(self):
		config = load_json(CONFIG_FILE_NAME, default={})
	
		if config and "default_recipient" in config:
			return config["default_recipient"]
			
		else:
			default_recipient, ok = show_prompt( 'First run - please enter default recipient' )
			config['default_recipient'] = default_recipient
			save_json(CONFIG_FILE_NAME, config)
	
			return default_recipient

class GpgDecrypt(DirectoryPaneCommand):
	def __call__(self):
		fileName = as_human_readable( self.get_chosen_files()[0] )
		gpg = GPG()
		myPass, ok = show_prompt('Passphrase')
		# https://stackoverflow.com/questions/4444923/get-filename-without-extension-in-python
		fileNameOut, ok = show_prompt( 'Target', default= os.path.splitext(fileName)[0] )
		with open(fileName, 'rb') as f:
			status = gpg.decrypt_file(
				f, passphrase = myPass,
				output = fileNameOut)
		show_alert('Status: ' + status.status)



