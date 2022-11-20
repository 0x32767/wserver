# Project structure

## Structure

The project structure of the website is strongly up to the developer. However, if you want to play by the book then in the root of the project there should be folders with the following names:

- components
- pages
- assets
- api
- resources

## components

Because a jsx-like syntax can be used it is recomended that there is a folder named components, this stores the components of the website, these can range from custom elements to a page layout. These can be accessed from anywere in the project.

## pages

Similar to ASP.NET there is a pages directory, this fill contain full pages, this should give a sort of overview of the page and assemble the components together.

## assets

Similar to react or unity there is an assets folder, this folder contains raw images and files that is required for the appeirence of the website. These should be static and non-exacutable programs.

## api

This rouse is rather self explanitory, this has non-page data and contains routes, these don't return a page to be rendered, instead they return data that can be used in the front end or in other aplications.
