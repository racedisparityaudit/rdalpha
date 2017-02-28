# == Schema Information
#
# Table name: topics
#
#  id          :integer          not null, primary key
#  name        :string
#  topic_id    :integer
#  description :string
#  uri         :string
#  created_at  :datetime         not null
#  updated_at  :datetime         not null
#

class Topic < ApplicationRecord
  belongs_to :topic
  has_many :topics

  def self.topic_level
    Topic.where(topic_id: nil)
  end

  def topic_level
    parent_name == "homepage"
  end

  def parent_name

  end
end
