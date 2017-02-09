class HomepageController < ApplicationController

  def index

    @topics = TaxonomyLevel.homepage.taxonomy_levels
  end
end
