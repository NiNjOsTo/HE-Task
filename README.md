# HE-challenge

This challenge will be split into two parts, a backend part and a front end.

Through this Challenge we'll mostly be looking to see your understanding of django and other frontend frameworks and your ability to go through someone else's code and find ways to improve it.

The backend is already made in **Django** and you'll be doing some minor modifications , but for the front end you'll need to create it from scratch in whatever technology you like (preferably React.js or Next.js).

***You have (5days) to be done with the whole challenge***

## For the Backend part 
you will need to clone this repo to be able to work on the tasks.

The tasks for the Backend are:
- Make an endpoint to fetch variants for a specific pacakge . **checked**
  http://127.0.0.1:8000/openapi/variant/packageid/:id

- Calculate if the variant has any future dates  and return it with the varaints response . **checked**
  http://127.0.0.1:8000/openapi/Variants/

- Add "mark as sold out" field to all tables (slot,date,variant,package) so admins/agents can set packages as sold out manually. **checked**

- Optimize get all pacakges endpoint. **checked**
  http://127.0.0.1:8000/openapi/Packages/


- Create new endpoint to get only active packages with future dates. **half-checked**
  http://127.0.0.1:8000/openapi/Packages/isactive/
  **only active couldn't manage to arrange it with future dates**
  
- Create new endpoint to update a variant's title and description. 
  http://127.0.0.1:8000/openapi/VariantsUpdate/1

#### **Bonus points for writing unit tests.**



## For the Frontend part 

- Make a list page to show all pakcages , the details shown should include : **checked**

  - Title **checked**
  - Agency Name **checked**
  - Country Name **checked**
  - Active status **checked**
  - sold out status **checked**

- You can choose a package and get redirected to a detail page that contains a list of variants related to the package **checked**
  the list should contain the following details
    - Title **checked**
    - has future dates **checked**
    - sold out status **checked**
  
  
