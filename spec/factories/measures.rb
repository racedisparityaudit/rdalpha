# == Schema Information
#
# Table name: measures
#
#  id          :integer          not null, primary key
#  name        :string
#  topic_id    :integer
#  description :string
#  uri         :string
#  source      :string
#  display     :string
#  subtitle    :string
#  created_at  :datetime         not null
#  updated_at  :datetime         not null
#

FactoryGirl.define do
  factory :measure do
    
  end
end
