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

  def self.metrics
    all.all.select{ |t| t.metric_level?}
  end

  def self.homepage
    TaxonomyLevel.where(parent_id:nil).first
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

  def display_name
    name.titleize
  end

  def metric_level?
    taxonomy_levels.empty?
  end

  def parent_name
    taxonomy_level.name
  end

end
