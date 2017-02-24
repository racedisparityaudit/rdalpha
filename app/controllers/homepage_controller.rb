class HomepageController < ApplicationController
  RACE = "race".freeze
  TOPIC = "topic".freeze
  LOCATION = "location".freeze

  def index
    @topics = TaxonomyLevel.homepage.taxonomy_levels
  end

  def navigation_form
    case params["filter_type"]
    when RACE
      race_redirect
    when TOPIC
      topic_redirect
    when LOCATION
      location_redirect
    else
      render 404
    end
  end

  private

  def race_redirect
    redirect_to "/factoids/" + "#{params['radio-group']}"
  end

  def topic_redirect
    redirect_to "/factoids/" + "#{params['radio-group']}"
  end

  def location_redirect
  end

end
