require File.dirname(__FILE__) + "/spec_helper.rb"
require 'wikipedia_article'

describe WikipediaArticle do

  context "creating a new article from a page id" do
    before :each do
      # FIXME: mock out HTTP request
      @article = WikipediaArticle.new(52780)
    end

    it "should return an object of type WikipediaArticle" do
      @article.class.should == WikipediaArticle
    end

    it "should have the correct URI" do
      @article.uri.to_s.should == 'http://dbpedialite.org/things/52780#thing'
    end

    it "should not have co-ordinates" do
      @article.should_not have_coordinates
    end
  end

  context "creating a new article from a page title" do
    before :each do
      # FIXME: mock out HTTP request
      @article = WikipediaArticle.new(nil, :title => 'U2')
    end

    it "should return an object of type WikipediaArticle" do
      @article.class.should == WikipediaArticle
    end

    it "should have the correct URI" do
      @article.uri.to_s.should == 'http://dbpedialite.org/things/52780#thing'
    end
  end

  context "creating a new article with data provided" do
    before :each do
      @article = WikipediaArticle.new(934787,
        :title => 'Ceres, Fife',
        :latitude => 56.293431,
        :longitude => -2.970134,
        :updated_at => DateTime.parse('2010-05-08T17:20:04Z'),
        :abstract => "Ceres is a village in Fife, Scotland."
      )
      # HACK
      @article.title = 'Ceres, Fife'
    end

    it "should return an object of type WikipediaArticle" do
      @article.class.should == WikipediaArticle
    end

    it "should have the correct URI" do
      @article.uri.to_s.should == 'http://dbpedialite.org/things/934787#thing'
    end

    it "should have the correct title" do
      @article.title.should == 'Ceres, Fife'
    end

    it "should have the correct abstract" do
      @article.abstract.should == 'Ceres is a village in Fife, Scotland.'
    end

    it "should have a pageid method to get the page id from the uri" do
      @article.pageid.should == 934787
    end

    it "should have the correct latitude" do
      @article.latitude.should == 56.293431
    end

    it "should have the correct longitude" do
      @article.longitude.should == -2.970134
    end

    it "should encode the Wikipedia page URL correctly" do
      @article.page.to_s.should == 'http://en.wikipedia.org/wiki/Ceres%2C_Fife'
    end

    it "should encode the dbpedia URI correctly" do
      @article.dbpedia.to_s.should == 'http://dbpedia.org/resource/Ceres%2C_Fife'
    end
  end

  context "serializing an article to N-Triples" do
    before :each do
      @article = WikipediaArticle.new(52780,
        :title => 'U2',
        :abstract => "U2 are an Irish rock band."
      )
      @ntriples = @article.dump(:ntriples)
    end

    it "should serialise to a string" do
      @ntriples.class.should == String
    end

    it "should serialise to 3 triples" do
      @ntriples.split(/[\r\n]+/).count.should == 3
    end
  end

  context "loading a page from wikipedia" do
    before :each do
      # FIXME: mock out HTTP request
      @article = WikipediaArticle.new(934787)
      @article.load
    end

    it "should had the correct page id" do
      @article.pageid.should == 934787
    end

    it "should had the correct title" do
      @article.title.should == 'Ceres, Fife'
    end

    it "should have co-ordinates" do
      @article.should have_coordinates
    end

    it "should have the correct latitude" do
      @article.latitude.should == 56.293431
    end

    it "should have the correct longitude" do
      @article.longitude.should == -2.970134
    end

    it "should encode the Wikipedia page URL correctly" do
      @article.page.to_s.should == 'http://en.wikipedia.org/wiki/Ceres%2C_Fife'
    end

    it "should encode the dbpedia URI correctly" do
      @article.dbpedia.to_s.should == 'http://dbpedia.org/resource/Ceres%2C_Fife'
    end

    it "should extract the abstract correctly" do
      @article.abstract.should =~ /^Ceres is a village in Fife, Scotland/
    end
  end
end
