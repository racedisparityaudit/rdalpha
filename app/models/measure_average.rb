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
  belongs_to :taxonomy_level

  def display_value
    value.to_d.round(1).to_s + " %"
  end

  def display_national
    national_value.to_d.round(1).to_s + " %"
  end
end
