
# Question 129727

**Question Title**: Migration!

**Question Link**: [Migration!](https://quera.org/problemset/129727) 

**Difficulty Level**: 🟠
## Question Description
- In this problem, we have to change the data structure of the model and replace the data according to these changes

## Approach

The key to resolving the issue with the `set_published` function is to handle the `updated` field properly. Since the `updated` field is set to `auto_now=True`, it will automatically update to the current time whenever the `save()` method is called on an `Article` instance. This means that after setting `article.updated = article.created` in the `set_published` function, the subsequent `article.save()` call will overwrite the value with the current timestamp.

To address this, you can either define the `updated` field without `auto_now=True`, allowing you to manually set the value as needed, or use the `F` expression to update the `published` and `updated` fields directly without triggering the automatic update behavior. By taking either of these approaches, you can ensure that the `published` and `updated` fields are properly set for all existing articles during the migration process.


## Key Points
- ORM django
- transaction.atomic
- migrations

## Sample Code
```python
@transaction.atomic
def set_published(apps, schema_editor):
    Article = apps.get_model('blog', 'Article')
    Article.objects.update(published=F('created'), updated=F('created'))
```



## Status

- **Completed**

## Learning
- [migrations-operations](./../../learn/migrations-operations.md)