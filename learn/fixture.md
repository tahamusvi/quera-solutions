# Guide to Using Fixtures in Django

## **Import From fixture file**

### **Step 1: Create Fixture File**
First, create a new file named `data.json` (or any other name you prefer) in the `fixtures` directory of your Django project.

### **Step 2: Define Fixture Data**
In the `data.json` file, define your desired data in JSON format. Each object in the JSON array represents a record in the database. Example:

```json
[
  {
    "model": "app_name.YourModel",
    "pk": 1,
    "fields": {
      "name": "John Doe",
      "email": "john@example.com",
      "created_at": "2023-04-15T10:30:00Z"
    }
  },
  {
    "model": "app_name.YourModel",
    "pk": 2,
    "fields": {
      "name": "Jane Smith",
      "email": "jane@example.com",
      "created_at": "2023-04-16T14:45:00Z"
    }
  }
]
```

Replace `app_name` with the name of your app, and `YourModel` with the name of your model.

###  **Step 3: Load Fixture**
In the terminal, run the following command to load the data from the `data.json` file into your database:

```
python manage.py loaddata data.json
```

### **Important Notes**
- The `fixtures` directory should be relative to your Django project root (usually one level above your app directory).
- Ensure that the JSON structure and its mapping to your models are correct.
- If you need to update the fixture data, you can edit the file and reload it.
- Using fixtures can be helpful in development, testing, and initial environment setup processes.


## **Export to Fixture file**


### **Step 1: Open the Django shell**
In your terminal, run the following command to open the Django shell:

   ```
   python manage.py shell
   ```

### **Step 2: Export the data**
In the Django shell, use the following code to export the data of your model to a JSON file:

   ```python
   from django.core import serializers
   from .models import YourModel  # Replace 'YourModel' with the name of your model

   data = serializers.serialize('json', YourModel.objects.all())

   with open('fixtures/your_model_data.json', 'w') as f:
       f.write(data)
   ```

   This code will:
   - Import the `serializers` module from `django.core`
   - Import your model
   - Serialize all objects of your model to JSON format using `serializers.serialize('json', YourModel.objects.all())`
   - Write the JSON data to a file named `your_model_data.json` in the `fixtures` directory

### **Step 3: Verify the JSON file**
Check the `fixtures` directory in your project to ensure that the `your_model_data.json` file has been created and contains the expected data.

Now, you can use this JSON file as a fixture in your Django project. Here's how:

#

## **Use YAML**

1. **Install PyYAML**: First, make sure you have the `PyYAML` library installed. If not, you can install it using pip:

   ```
   pip install pyyaml
   ```

2. **Create a YAML fixture file**: Instead of the JSON file, you can create a YAML file with the fixture data. For example, create a file named `seats.yaml` in your `fixtures` directory with the following content:

   ```yaml
   - model: app.Seat
     pk: 1
     fields:
       seat_number: 31
   - model: app.Seat  
     pk: 2
     fields:
       seat_number: 32
   - model: app.Seat
     pk: 3
     fields:
       seat_number: 33
   # Add more seats as needed
   ```

   This YAML file defines the same 10 seats as the previous JSON example.

3. **Load the YAML fixture**: To load the YAML fixture, you can use the same `loaddata` management command, but specify the YAML file instead of the JSON file:

   ```
   python manage.py loaddata seats.yaml
   ```

   Django will automatically detect the YAML format and load the data into the database.

4. **Serialize data to YAML**: If you want to export data from your models to a YAML fixture, you can use the following code in the Django shell:

   ```python
   from django.core import serializers
   from .models import Seat

   data = serializers.serialize('yaml', Seat.objects.all())

   with open('fixtures/seats.yaml', 'w') as f:
       f.write(data)
   ```

   This code will serialize all the `Seat` objects to a YAML format and save them in the `seats.yaml` file.

The main advantages of using YAML for fixtures are:

- YAML is generally more human-readable and can be easier to maintain, especially for larger datasets.
- YAML supports comments, which can be useful for documenting the fixture data.
- YAML files can be easily edited using a text editor, which can be helpful during development and testing.
