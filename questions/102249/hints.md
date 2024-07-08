
# Question 16400

**Question Title**: Command Line

**Question Link**: [Command Line](https://quera.org/problemset/102249) 

**Difficulty Level**: 🔴/🟠/🟢
## Question Description
We are going to make some djanog custom commands with different intentions towards working with our company model. For example adding new company or editting the existing company pr removing companies or taking an out put of the companies info in a csv file, all by using command line.

## Approach
First in the app dir i made management folder and then onother folder in this folder called command. I made four .py files in command folder, the name of the files are the command arg to excute them. 
addCompany.py
editCompany.py
rmCompany.py
collectComapny.py

So whats going on in each of these files? At first we have two important imports:
from career.models import Company
from django.core.management.base import BaseCommand,CommandError

Then we create a Command class wich inherits the  BaseCommand
Typically this class as two methods, one called add_argument and the other called handle.
When there is no command prompts or inputs neede from the user, you can skip the add_arguments method


## Key Points
- [List the key points, concepts, or techniques that are important to understand in order to solve this question.]
- [For example, if the question is about Django models, you can mention topics like field types, relationships, and model methods.]

## Sample Code
```python
class Command(BaseCommand):
    help = 'Edit company information'
    def add_arguments(self, parser):

                # Positional argument: company name
        parser.add_argument('company_name', type=str)

                # Optional arguments
        parser.add_argument('--description', type=str)
        parser.add_argument('--phone', type=str)
        parser.add_argument('--email', type=str)
        parser.add_argument('--name', type=str)

    def handle(self, *args, **options):
            company_name = options['company_name']
            description = options['description']
            phone = options['phone']
            email = options['email']
            name = options['name']
            Company.objects.create(name=name, email=email, phone=phone, description=description )
            print(f'Company {company.name} has been updated.')

   Pay attentio nto the difference of the positional and optional args in the add_argument method

   In handle you can do lots of data validation and you can user self.stderr.write(error_msg) to print an error or use CommandError to throw and exception


```

## Additional Resources
Well I read lots of docs and watched lots of youtube tutorails

## Status
Work in progress

- **Completed**
- **Pending**
- **Work in Progress**
- **Under Review**

## Learning

- Django Custom Commands