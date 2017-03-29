class TaxonomyLevelController < ApplicationController
  FILLED_OUT_URIS = [
     "/education/schoolsandcolleges/1/averagegcsegradeattainment8",
     "/housingandlivingstandards/socialandaffordablehousing/accesstosocialhousing/housingandliving16"
  ]

  def show
    @taxonomy_level = TaxonomyLevel.find_by_name(params[:taxonomy_name])
    @chart_tabs = @taxonomy_level.chart_tabs
    @js_flag = @taxonomy_level.js_flag

    @measure_explanation = markdown_to_html(@taxonomy_level.measure_explanation)
    @overall_summary = markdown_to_html(@taxonomy_level.overall_summary)
  end

  def markdown_to_html(markdown)
    doc = Govspeak::Document.new markdown
    doc.to_html
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
