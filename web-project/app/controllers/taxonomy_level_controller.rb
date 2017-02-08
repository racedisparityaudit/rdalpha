class TaxonomyLevelController < ApplicationController

  def show
    @taxonomy_level = TaxonomyLevel.find_by_name(params[:taxonomy_name])
    @topics  = TaxonomyLevel.find_by_name(params[:taxonomy_name]).taxonomy_levels
  end

  def question

  end

end
