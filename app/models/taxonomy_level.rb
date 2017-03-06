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
#  subtitle    :string
#

class TaxonomyLevel < ApplicationRecord
  has_many :taxonomy_levels, foreign_key: :parent_id
  belongs_to :taxonomy_level, foreign_key: :parent_id
  has_many :measure_averages
  HOMEPAGE_NAME = "homepage"

  def self.metrics
    all.select{ |t| t.metric_level?}
  end

  def self.homepage
    TaxonomyLevel.where(parent_id: nil).first
  end

  def self.topics
    TaxonomyLevel.where(parent_id: homepage.id)
  end

  def anchor
    name.split(" ").join("")
  end

  def breadcrumbs
    [TaxonomyLevel.homepage , top_level_parent]
  end

  def link
    if uri == TaxonomyLevel.homepage.uri
      "/"
    else
      "/topics/#{top_level_parent.id}"
    end
  end

  def measures
    metric_level? ? self : taxonomy_levels.map(&:measures).flatten
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

  def national
    return nil unless measure_averages.any?
    measure_averages.first.display_national
  end

  def group_average(group)
    return "-" unless group && number =  measure_average_for(group).try(:display_value)
    display_encode(number)
  end

  def display_name
    title.downcase.tap{ |n| n[0] = n.first.upcase }.gsub("&","and")
  end

  def metric_level?
    taxonomy_levels.empty?
  end

  def parent_name
    taxonomy_level.name
  end

  private

  def title
    name == HOMEPAGE_NAME ? "Entire public sector" : name
  end

  def measure_average_for(group)
    measure_averages.select{ |a| a.subgroup_name.downcase == group.downcase }.first
  end

  def display_encode(number_string)
    # TODO: awful it gets confused because of use of keyword
    if self[:display] == "percent"
      (number_string.to_d * 100).round(1).to_s + " %"
    else
      number_string.to_d.round(2).to_s
    end
  end

end
