class TaxonomyLevelController < ApplicationController
  FILLED_OUT_URIS = [
     "/education/schoolsandcolleges/resultsandstudentprogress/attainment8",
     "/housingandlivingstandards/socialandaffordablehousing/accesstosocialhousing/housingandliving16"
  ]

  def show
    @taxonomy_level = TaxonomyLevel.find_by_name(params[:taxonomy_name])
    case @taxonomy_level.uri
    when "/education/schoolsandcolleges/resultsandstudentprogress/attainment8"
      @presenter = Attainment8.new
      render("attainment8")
    when "/work/employment/participationinthelabourmarket/unemploymentrate"
      @presenter = Unemployment.new
      render("unemployment")
    when "/housingandlivingstandards/socialandaffordablehousing/accesstosocialhousing/housingandliving16"
      render('question')
    end
    @presenter = Attainment8.new
  end

  def metadata
  end

  def question
  end

  def factoids
    race = params[:race]
    redirect_to "/topics/#{TaxonomyLevel.homepage.id}/#{race}"
  end

  def topics
    @topic =
      if params[:filter] == "all"
        TaxonomyLevel.homepage
      else
        TaxonomyLevel.find(params[:filter])
      end
    @taxonomy_level = @topic
    @race = params[:race]
  end

  private

  class Factoid
    attr_reader :question

    def initialize(taxonomy_level)
      throw RuntimeError unless taxonomy_level.metric_level?
      @question = taxonomy_level.description
    end
  end
end
