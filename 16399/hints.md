# Translation



1. **Create the locale folder**: First, you need to create a `locale` folder in your Django project's root directory or in any apps directory.

2. **Add LOCALE_PATHS**:

    Add LOCALE_PATHS, this is where your translation files will be stored.
    ```
    LOCALE_PATHS = (
       os.path.join(BASE_PATH, 'locale/'),
    )
    ```


3. **Create the language-specific folder**:

    use this command can create files you need for translation.
    ```
    manage.py makemessages -l fa
    ```

    - fa: farsi
    - en: english 


4. **Add the translation entries**: 
    
    Open the django.po file and add the following entries.
    ```
    #: templates/your_template.html:8
    msgid "Number of visits"
    msgstr "Number of visits"

    #: templates/your_template.html:12
    msgid "Your website had {{ visits }} visits yesterday."
    msgstr "Your website had {{ visits }} visits yesterday."
    ```



    The `msgid` is the original string in the HTML file, and `msgstr` is the translation. In this case, we're keeping the translations the same as the original strings, but you can replace them with the desired translations.

5. **Compile the translation file**: 
    Once you've added the translation entries, you need to compile the `django.po` file into a binary `.mo` file that Django can use. You can do this by running the following command in your project's root directory:

    ```
    django-admin compilemessages
    ```

    This will generate the `.mo` file in the same `en` folder.


6. **Use the translated strings in your HTML file**:

    Now, in your HTML file, you can use the translated strings as before

    ```html
    {% load i18n %}

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{{ title }}</title>
    </head>

    <body>

    <h1>{{ title }}</h1>

    <h2>{% trans "Number of visits" %}</h2>

    <p>
        {% blocktrans trimmed %}
            Your website had {{ visits }} visits yesterday.
        {% endblocktrans %}
    </p>

    </body>
    </html>
    ```

    When the user's browser is set to English, Django will automatically display the translated strings from the `django.po` file.

