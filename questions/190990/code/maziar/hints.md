# Question 190990

**Question Title**: Queries of QueraShop

**Question Link**: [Queries of QueraShop](https://quera.org/problemset/190990) 

**Difficulty Level**: 🟢

## Question Description
Recently, Quera established a store called QueraShop and wants to have easy access to the information stored in the database of the store. So we are going to write some queries to get this information.

## Key Points
Being able to work with Djnago's ORM to write complex queries, Being able to use annotate or aggregate functions at the right place and having a deep insight of the ways to query data from the database



## Sample Code
```python
def nonprofitable_companies():
      # Filter products that have been sold less than 100 times
    low_sales_products = Product.objects.annotate(sold_count=Count('order')).filter(sold_count__lt=100)
    
    # Filter companies with at least 4 products that have low sales
    low_sales_company_names = (
        Company.objects.filter(product__in=low_sales_products)
        .annotate(low_sales_product_count=Count('product'))
        .filter(low_sales_product_count__gte=4)
        .values_list('name', flat=True)
    )

    return list(low_sales_company_names)
```



## Status
Completed

- **Completed**
- **Pending**
- **Work in Progress**
- **Under Review**


## Learning