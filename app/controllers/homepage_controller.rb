class HomepageController < ApplicationController
  RACE = "race".freeze
  TOPIC = "topic".freeze
  LOCATION = "location".freeze

  def index
    @homepage = true
    @title =
      case params[:number]
      when nil
        "Race disparity in public services"
      when "1"
        "Government data on ethnicity"
      when "2"
        "Ethnicity in Britain today"
      when "3"
        "Ethnic inequality statistics"
      when "4"
        "Public services ethnicity metrics"
      when "5"
        "Ethnicity statistics "
      end
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
    #TODO: change race radios to race-radio-group for consistency
    redirect_to "/factoids/" + "#{params['radio-group']}"
  end

  def topic_redirect
    # TODO: could use taxonomy level URI's (stored on model) to handle navigation
    # using name doesn't really work because they have to be encoded for urls
    redirect_to "/topics/" + "#{params['topic-radio-group']}"
  end

  def location_redirect

  end

end
