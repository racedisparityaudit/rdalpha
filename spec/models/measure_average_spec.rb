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

require 'rails_helper'

RSpec.describe MeasureAverage, type: :model do
  pending "add some examples to (or delete) #{__FILE__}"
end
