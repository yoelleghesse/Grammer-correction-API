The LanguageTool Spell and Grammar Checker is a Python script that utilizes the LanguageTool API to perform spell and grammar checks on provided text. It sends a POST request to the LanguageTool API endpoint with the text to be checked and the desired language (automatically detected), then parses the API response to retrieve the spell and grammar check results.

Clone the repo:

``git clone https://github.com/your-username/language-tool-checker.git``

Install the required dependencies:

``pip install requests``

Run the script with the desired text to be checked:

``python spell_grammar_checker.py``

Ex.

``text = 'henlo'
print(spell_check(text))``

You may modify the text variable in the script to provide different text inputs for spell and grammar checking.
