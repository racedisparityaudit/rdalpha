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
#

class TaxonomyLevel < ApplicationRecord
  has_many :taxonomy_levels, foreign_key: :parent_id
  belongs_to :taxonomy_level, foreign_key: :parent_id


  def display_name
    name.titleize
  end

  def parent_name
    taxonomy_level.name
  end

  def self.homepage
    TaxonomyLevel.where(parent_id:nil).first
  end
end
