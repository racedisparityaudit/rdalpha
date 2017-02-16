# == Schema Information
#
# Table name: taxonomy_levels
#
#  id          :integer          not null, primary key
#  level       :string
#  name        :string
#  parent_name :string
#  parent_id   :integer
#  created_at  :datetime         not null
#  updated_at  :datetime         not null
#  description :string
#  uri         :string
#  source      :string
#  display     :string
#  white       :string
#  mixed       :string
#  asian       :string
#  black       :string
#  chinese     :string
#  national    :string
#

class TaxonomyLevel < ApplicationRecord
  has_many :taxonomy_levels, foreign_key: :parent_id
  belongs_to :taxonomy_level, foreign_key: :parent_id

  def self.metrics
    all.select{ |t| t.metric_level?}
  end

  def self.homepage
    TaxonomyLevel.where(parent_id: nil).first
  end

  def self.topic_level
    TaxonomyLevel.where(parent_id: homepage.id)
  end

  def breadcrumbs(crumbs = [])
    crumbs << name
    return crumbs unless taxonomy_level

    taxonomy_level.breadcrumbs(crumbs)
  end

  def top_level_parent
    # TODO: will blow up if there is no taxonomy_level
    return self if topic_level?
    return taxonomy_level.top_level_parent
  end

  def topic_level?
    parent_name == "homepage"
  end

  def subtitle
    self[:subtitle] || "Description unavailable."
  end

  def national_average
    return "-" unless national
    display_encode(national)
  end

  def black_average
    return "-" unless black
    display_encode(black)
  end

  def display_name
    name.titleize
  end

  def metric_level?
    taxonomy_levels.empty?
  end

  def parent_name
    taxonomy_level.name
  end

  private

  def display_encode(number_string)
    # TODO: awful it gets confused because of use of keyword
    if self[:display] == "percent"
      # binding.pry
      (number_string.to_d * 100).round(1).to_s + " %"
    else
      number_string.to_d.round(2).to_s
    end
  end

end
