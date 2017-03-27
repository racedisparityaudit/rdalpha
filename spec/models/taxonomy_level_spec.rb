
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

require 'rails_helper'

RSpec.describe TaxonomyLevel, type: :model do

  it "should load the correct json file" do
    taxonomy_level = FactoryGirl.create :taxonomy_level, uri: "/test/measure/measure_name"
    expect(taxonomy_level.json_uri).to eq(Rails.root.join("/data/pages#{taxonomy_level.uri}/data.json"))

  end

  # it "should give all of the bottom level children for a topic" do
  # end

  # it "should have a homepage" do
  # end

  # it "should have the homepages direct children as topics" do
  # end

  # it "should find the topic for a t4 page" do
  # end

end
