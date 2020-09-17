This app is deployed to Heroku where it can be used as a CMS:

 * View the site at https://fast-gorge-49964.herokuapp.com
 * Use Django Admin as a CMS at https://fast-gorge-49964.herokuapp.com/admin

 However, it's not persisted or served from there for the public. They see a static version hosted by Github Pages at https://kimstrudwick.com

 The source for both the static site and the Django CMS are mixed together in one repo at https://github.com/kimstrudwick/kimstrudwick.github.io/.

 To update the static site, visit the `cms` Github Actions workflow and run it. This scrapes the Heroku site and commits it to the repo, and hence updates the Github Pages site.

 If the CMS/Heroku version has no images, it's because the heroku persistent storage has been cycled.  Redeploy thus:

     # Fetch any auto-committed media assets that have been made static (i.e. the contents of `media/`)
     git pull origin master

     # Redeploy, including the previously-ephemeral media assets
     git push heroku master


