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

require 'rails_helper'

RSpec.describe TaxonomyLevel, type: :model do
  pending "add some examples to (or delete) #{__FILE__}"
end
