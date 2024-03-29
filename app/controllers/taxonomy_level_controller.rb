class TaxonomyLevelController < ApplicationController
  FILLED_OUT_URIS = [
     "/education/schoolsandcolleges/resultsandstudentprogress/attainment8",
     "/housingandlivingstandards/socialandaffordablehousing/accesstosocialhousing/housingandliving16"
  ]

  def show
    @taxonomy_level = TaxonomyLevel.find_by_name(params[:taxonomy_name])
    if @taxonomy_level.metric_level?
      case @taxonomy_level.uri
      when "/education/schoolsandcolleges/resultsandstudentprogress/attainment8"
        render("attainment8")
      when "/housingandlivingstandards/socialandaffordablehousing/accesstosocialhousing/housingandliving16"
        render('question')
      else
        render('missing')
      end
    else
      # TODO: KASM fix logic so there are never any loops
      @topics  = TaxonomyLevel.find_by_name(params[:taxonomy_name]).taxonomy_levels
                    .reject { |level| level.name == @taxonomy_level.name }
    end
  end

  def question

  end

  def factoids
    @filter = params[:filter]
    @factoids = TaxonomyLevel.metrics
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
