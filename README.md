# django_exercise

## Python 3.7.5

The command is called getInterfaces and can be called with python manage.py getInterfaces

## Description

Create an Django command that will pull hardware data from two separate HTTP endpoints 
and save the data as a new resource.

## Instructions

1. Fork this project.

2. Create a model named `MonitoredInterface` with the following fields:

    - external_id
        ```
          Will store the value of the external resources unique identifier. 
        ```
    - mac_address
        ```
          The mac address of the interface. This field should conform to the format of 12 characters, 
          with only the characters A-F/0-9 allowed. e.g. A1B2C3D4E5F6
        ```
    - ipv4_address
        ```
          The ipv4 address of the interface.
        ```
    - interface_name
        ```
          The name of the interface.
        ```
    - created_at
        ```
          The date and time of record creation.
        ```
    - updated_at
        ```
          The date and time of when the record was last updated.
        ```
      
    The `mac_address` and `interface_name` should be unique together.
      
 3. Create a Django command that sends HTTP requests to each of the base URLs (found in `.env.example`) and
    creates or updates `MonitoredInterface` records with the results.
    
 4. Open a merge request once you are finished.
