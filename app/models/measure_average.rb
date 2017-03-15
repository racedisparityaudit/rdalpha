# == Schema Information
#
# Table name: measure_averages
#
#  id                :integer          not null, primary key
#  uri               :string
#  value             :string
#  subgroup_name     :string
#  group_name        :string
#  national_value    :string
#  taxonomy_level_id :integer
#  created_at        :datetime         not null
#  updated_at        :datetime         not null
#

class MeasureAverage < ApplicationRecord

  RACE_CATEGORIES = [
      "White All",
      "English / Welsh / Scottish / Northern Irish / White British",
      "Irish",
      "Gypsy or Irish Traveller",
      "Mixed All",
      "White and Black Caribbean",
      "White and Black African",
      "White and Asian",
      "Any other Mixed / Multiple ethnic background",
      "Asian All",
      "Indian",
      "Pakistani",
      "Bangladeshi",
      "Chinese",
      "Any other Asian background",
      "Black All",
      "African",
      "Caribbean",
      "Any other Black / African / Caribbean background",
      "Arab",
      "Other"
    ].freeze

  def self.generate_test_data
    TaxonomyLevel.homepage.measures.each do |measure|
      RACE_CATEGORIES.each{ |subgroup| create_dummy_measure_average(measure, subgroup) }
    end
  end

  def self.create_dummy_measure_average(measure,subgroup)
    return if Random.rand > 0.8
    MeasureAverage.create(taxonomy_level_id: measure.id, subgroup_name: subgroup, national_value: 0.4 + Random.rand * 0.2, value: 0.4 + Random.rand * 0.2)
  end

  def self.exists?(category,topic_name)
    category.measure_averages.map(&:subgroup_name).include?(topic_name)
  end

  def display_value
    value.to_d
  end

  def display_national
    national_value.to_d
  end

end
