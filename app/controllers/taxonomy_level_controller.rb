class TaxonomyLevelController < ApplicationController

  def show
    @taxonomy_level = TaxonomyLevel.find_by_name(params[:taxonomy_name])
    if @taxonomy_level.metric_level?
      @taxonomy_level.uri ==  "/housingandlivingstandards/socialandaffordablehousing/accesstosocialhousing/housingandliving16" ? render('question') : render('missing')
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
end
