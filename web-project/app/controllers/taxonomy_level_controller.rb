class TaxonomyLevelController < ApplicationController

  def show
    @taxonomy_level = TaxonomyLevel.find_by_name(params[:taxonomy_name])
    if @taxonomy_level.metric_level?
      @taxonomy_level.uri ==  "/housingandlivingstandards/socialandaffordablehousing/accesstosocialhousing/housingandliving16" ? render('question') : render('missing')
    else
      @topics  = TaxonomyLevel.find_by_name(params[:taxonomy_name]).taxonomy_levels
    end
  end

  def question

  end

end
