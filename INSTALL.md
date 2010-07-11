# Installing dbpedialite on your machine

Clone the repo
 
   git clone git://github.com/njh/dbpedialite.git
   cd dbpedialite

Install the required gems. If you're using bundler

   bundle install

Otherwise

   [sudo] gem install sinatra spira sinatra-content-for rdiscount rdf-json rdf-rdfxml

Start the application
 
   ruby dbpedialite.rb

Visit the application in your browser at http://localhost:4567/

To run the tests you'll also need the [Raptor
RDF](http://librdf.org/raptor/rapper.html) parser. A simple way to
install this on Mac OS X is using
[homebrew](http://github.com/mxcl/homebrew)

   brew install raptor

Or using [fink](http://fink.sf.net/):

   fink install raptor

Or on Debian GNU/Linux:

   apt-get install raptor